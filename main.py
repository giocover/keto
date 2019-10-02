import os
import numpy as np
import nrrd as nd
import matplotlib.pyplot as plt 

dir_path = ('C:/Users/FarivarLabPC/OneDrive - McGill University/Research/Keto Project/subjects/')
os.chdir(str(dir_path))

subjects = [d for d in os.listdir('.') if os.path.isdir(d)]
subjects = np.array(subjects)

images = ['Start_Image','Follow Up']
save_path = 'C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Keto Project\\'

total_loss_s = np.zeros((len(subjects), 1)) 
total_loss_f = np.zeros((len(subjects), 1)) 
loss = np.zeros((len(subjects), len(images))) 

print("\n ############# Starting Program ############# ")
      
for n, m in enumerate(subjects):
#    if True:
    try:
        print("#---------------------------------------#\n")
        print(">>> subject being analysed: "+str(m)+"\n")
        print(">>> subject number "+str(n+1)+" of "+str(len(subjects))+"\n")
        for j, k in enumerate(images):

            seg_path = str(dir_path)+str(m)+'/'+str(k)+'/lesion_seg_judith_0.nrrd'
            ct_path = str(dir_path)+str(m)+'/'+str(k)+'/ct_image.nrrd'
            readdata, header = nd.read(seg_path)
            
            axial = [int(a) for a in readdata.shape]
            master = np.zeros((axial[2], 1)) 
            
            for slice in range(0,readdata.shape[2]):
                
                readdata, header = nd.read(seg_path)
                segmentation = np.transpose(readdata[:,:,slice])
                
                seg_corrected = segmentation
                
                ct_readdata, header = nd.read(ct_path)
                ct_image = np.transpose(ct_readdata[:,:,slice])
            
                head_dim = header['space directions']
                pixel_len = head_dim[0,0]
                pixel_wid = head_dim[1,1]
                slice_th = head_dim[2,2]
                
                lesion_size = np.sum(seg_corrected == 1)
                lesion_volume = lesion_size*pixel_len*pixel_wid*slice_th
            
                master[slice] = lesion_volume 
                
            try:
                directory = str(save_path)+'files\\'+str(m)
                os.makedirs(directory)
                print(">>> creating folder \n")
            except OSError:
                pass
            
            total_loss = np.sum(master)
            
            print(">>> saving lesion volume "+str(k)+" \n")
            np.save(str(directory)+'\\lesion_volume_'+str(m)+'_'+str(k), master)
            print(">>> saving total_loss "+str(k)+" \n")
            np.save(str(directory)+'\\total_loss_'+str(m)+'_'+str(k), total_loss)

          
        loss_s = (np.load(str(directory)+'\\total_loss_'+str(m)+'_'+str(images[0])+'.npy')/1000)
        loss_f = (np.load(str(directory)+'\\total_loss_'+str(m)+'_'+str(images[1])+'.npy')/1000)
        
        total_loss_s[n] = loss_s
        total_loss_f[n] = loss_f

        print(">>> saving total loss s \n")
        np.save(str(directory)+'\\total_loss_s_'+str(m), total_loss_s)
        print(">>> saving total loss f \n")
        np.save(str(directory)+'\\total_loss_f_'+str(m), total_loss_f)
        
    except:
        pass

loss = np.vstack((total_loss_s.T,total_loss_f.T))
np.save(str(save_path)+'\\master_loss',loss)

fig_1 = plt.figure()

p1 = plt.bar(np.arange(len(subjects)), loss[0,:], width = 0.35)
p2 = plt.bar(np.arange(len(subjects)), loss[1,:], width = 0.35)

plt.legend(images)
plt.xticks(np.arange(len(subjects)), subjects)
plt.xticks(rotation=80)
plt.yticks(loss.flatten('F'))
plt.grid(True, color = "#a6a6a6", linestyle='dotted') 
plt.xlabel('subject number') 
plt.ylabel(u'lesion volume [cm\u00b3]') 
plt.savefig(str(save_path)+'\\total_loss', dpi=600, transparent=True, bbox_inches='tight')

print("############# Program Ended ############# \n")

      #%%
l = loss.T
percentage = np.zeros((len(l)))
subtraction = np.zeros((len(l)))

for i in range(len(l)):
        a = l[i,0] 
        b = l[i,1]
        per = b*100/a
        sub = a-b
        percentage[i] = per 
        subtraction[i] = sub
        
matrix = np.vstack((percentage,subtraction))
matrix = np.vstack((l.T,matrix))  

sub = ['1412244', '5182095', '5241082', '5248966', '5250338', '5268985',
       '5327976', '5344003', '5352962', '5358570', '5368664', '5397598',
       '5411704', '5435796']

matrix = np.vstack((sub,matrix))

matrix = np.vstack((np.arange(1,len(subtraction)+1),matrix))
h = ['position','id','start_volume','follow_up_volume','percentage','subtraction']
matrix = np.vstack((h,matrix.T)) 

np.save(str(save_path)+'\\final_matrix',matrix)
np.savetxt(str(save_path)+"\\final_matrix.csv", matrix, delimiter=",", fmt='%s', comments='')
