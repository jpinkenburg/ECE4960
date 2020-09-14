<style>
    ul li { margin-bottom: 10px; }
</style>
<img src=https://mail.google.com/mail/u/0?ui=2&ik=91ff722dce&attid=0.1.1&permmsgid=msg-f:1677237112175478034&th=1746be4463524512&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ-Qww01AQ5_ZlbyN_LXbOX-HM_EcYCpbxX0q07lvVrB-bJ2L8hXtRD4dW6lC3clLCZCbq-VkklP_OCzhqozXpU1pd4x_ULVAq7nnqyYLG2URc6bvaJVrHHutJw&disp=emb" alt>
<Center> <h1>About Me</h1></Center>
Hi! My name is Jade and I'm super excited to take this class! Here are some (hopefully) fun facts about me:
<li> I'm currently a junior studying ECE and minoring in robotics </li>
 
<li> I think robots and autonomous systems are super cool - in high school I did a lot with FIRST robotics and I'm a member of CUAir and the Organic Robotics Lab here at Cornell</li>
 
<li> When I'm not being a stereotypical engineer in the lab, I enjoy playing the keyboard (not the typing kind!), running, hiking, and any sort of adventure I might stumble into</li>
 
<li> I'm trying to learn how to cook and don't consider myself so bad at it, but my smoke detector begs to differ </li>

<Center> <h1> Lab 1 </h1>
    <h2> <i> The Artemis Board </i></h2> </Center>

<h3 style="color: green;"> Setup </h3>
To be able to program the Artemis board, I first had to configure my Arduino IDE to install the required libraries. After installing everything, I checked that the programmer was functional by uploading the provided 'Blink It Up' program - as shown in the video below, the board exhibited the expected behavior (built in blue LED toggles every second).
++Insert Video Here++
<h3 style="color: green;"> Example Programs </h3>
<b> Serial Output: </b> To test if serial communication worked between my laptop and the Artemis board, I uploaded the provided 'Example2_Serial' program. As seen in the video below, the board was able to receive keyboard input from the laptop, process it, and print statements on my screen via the serial interface.<br>
++Insert Video Here++<br>
<b> Analog Tests: </b> To determine if the board is able to measure analog values, I ran the 'Example4_analogRead' program that reads an onboard temperature sensor and prints the output on the Arduino IDE via serial. In the video below, we can see the temperature of the board increase as I hold it close to my overheating laptop. <br>
![](Temp.MOV)<br>
<b> Microphone Test: </b> To see if the onboard microphone is functional, I uploaded the 'Example1_MicrophoneOuput' program that identifies the loudest frequency heard by the microphone. As seen in the video below, the loudest frequency changes with the pitch of the whistled tone.<br>
++Insert Video Here++<br>

<h3 style="color: green;"> Battery Tests </h3>
Another cool feature of the Artemis board is its onboard battery charger. When the LiPo battery is connected to the board while plugged into a laptop via USB-C, the board is able to charge the battery (indicated by the yellow light in the image below). When the board is disconnected from the computer, it is able to source power from the battery; this can be seen in the video below, in which the board turns on the blue built in LED when it detects a tone being whistled.<br>
++Insert Picture++<br>
++Insert Video++
