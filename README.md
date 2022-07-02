# Face-Detection-Flask

![Screenshot 2022-06-24 171349](tutorial\Screenshot 2022-06-24 171349.jpg)

Flask App for deploy deep learning model, work on Azure.

Replace your *.h5 model in models folder and replace in config.by



**Run**

Terminal: flask run![Screenshot 2022-06-24 180551](tutorial\Screenshot 2022-06-24 180551.jpg)

**Demo**

curl -X POST -F image=@test1.jpg 'http://127.0.0.1:5000/detect'

![](tutorial\Screenshot 2022-06-25 075449.jpg)![](tutorial/Screenshot%202022-06-24%20194639.jpg)