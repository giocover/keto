# keto

This python script reads from the selected path and loads a lesion segmentation file and a CT image. As a result, it computes the total volume of the lesion per subject and outputs a table with all results. The table should look like this:

![image_2](https://user-images.githubusercontent.com/32575426/66068037-d7909d00-e51a-11e9-9981-2c0ac6568791.PNG)

* To add the path, the following variable should be altered:

<pre><code>dir_path</code></pre>

* To select where results will be saved, the following variable should be edited:

<pre><code>save_path</code></pre>

As an output, the table can be used to generate graphs using the Latex source also added here. As a result, graphs should look like this:

![image](https://user-images.githubusercontent.com/32575426/66067725-2d187a00-e51a-11e9-97f1-86fd44b7c730.PNG)
