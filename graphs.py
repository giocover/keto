import os
import numpy as np
import matplotlib.pyplot as plt 

dir_path = ('C:/Users/FarivarLabPC/OneDrive - McGill University/Research/Keto Project/subjects/')
os.chdir(str(dir_path))

subjects = [d for d in os.listdir('.') if os.path.isdir(d)]
subjects = np.array(subjects)

images = ['Start_Image','Follow Up']
save_path = 'C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Keto Project\\'

for n, m in enumerate(subjects):
#    if True:
    try:
        for j, k in enumerate(images):        
            
            total_loss_loss_s = (np.load(str(save_path)+'files\\'+str(m)+'\\'+'total_loss_s_'+str(m)+'.npy'))
            total_loss_loss_f = (np.load(str(save_path)+'files\\'+str(m)+'\\'+'total_loss_f_'+str(m)+'.npy'))
            
            total_loss = np.load(str(save_path)+'files\\'+str(m)+'\\'+'total_loss_'+str(m)+'_'+str(k)+'.npy')
            
            master = np.load(str(save_path)+'files\\'+str(m)+'\\'+'lesion_volume_'+str(m)+'_'+str(k)+'.npy')
            
            x = np.arange(0,master.size) 
            y = (master[:,0]/1000)
            
            fig_0 = plt.figure(n)
            
            mectric = str(k)+u' %.1f cm\u00b3'% (total_loss/1000)
            plt.plot(x, y, label = mectric, linestyle='--') 
            plt.xlabel('axial slice') 
            plt.ylabel(u'lesion volume [cm\u00b3]') 
            
            plt.grid(True, color = "#a6a6a6", linestyle='dotted') 
            plt.legend() 
            plt.title('subject: '+str(m)) 
            
#            plt.savefig(str(save_path)+'graphs\\'+str(m), dpi=600, transparent=True, bbox_inches='tight')
    except:
        pass    