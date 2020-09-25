<style>
    ul li { margin-bottom: 10px; }
</style>
<Center> <img src="me.jpg" alt="Jade"><br>
<h1>About Me</h1></Center>
Hi! My name is Jade and I'm super excited to take this class! Here are some (hopefully) fun facts about me:
<li> I'm currently a junior studying ECE and minoring in robotics </li>
 
<li> I think robots and autonomous systems are super cool - in high school I did a lot with FIRST robotics and I'm a member of CUAir and the Organic Robotics Lab here at Cornell</li>
 
<li> When I'm not being a stereotypical engineer in the lab, I enjoy playing the keyboard (not the typing kind!), running, hiking, and any sort of adventure I might stumble into</li>
 
<li> I'm trying to learn how to cook and don't consider myself so bad at it, but my smoke detector begs to differ </li>

<Center> <h1> Lab 1 </h1>
    <h2> <i> The Artemis Board </i></h2> </Center>

<h3 style="color: green;"> Setup </h3>
To be able to program the Artemis board, I first had to configure my Arduino IDE to install the required libraries. After installing everything, I checked that the programmer was functional by uploading the provided 'Blink It Up' program - as shown in the video below, the board exhibited the expected behavior (built in blue LED toggles every second).
<iframe width="560" height="315" src="https://www.youtube.com/embed/OfnUbPsn1BE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
<h3 style="color: green;"> Example Programs </h3>
<b> Serial Output: </b> To test if serial communication worked between my laptop and the Artemis board, I uploaded the provided 'Example2_Serial' program. As seen in the video below, the board was able to receive keyboard input from the laptop, process it, and print statements on my screen via the serial interface. The provided example program actually didn't work perfectly because it neglected to take into account the default newline character when sending serial commands, so I had to alter the code slightly to make it run more smoothly.<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/wWjGUYQRyek" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
<b> Analog Tests: </b> To determine if the board is able to measure analog values, I ran the 'Example4_analogRead' program that reads an onboard temperature sensor and prints the output on the Arduino IDE via serial. In the video below, we can see the temperature of the board increase as I hold it close to my overheating laptop. <br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/1t-gQvpS2A4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
<b> Microphone Test: </b> To see if the onboard microphone is functional, I uploaded the 'Example1_MicrophoneOuput' program that identifies the loudest frequency heard by the microphone. As seen in the video below, the loudest frequency changes with the pitch of the whistled tone.<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7lypdgFtBKc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>

<p style="color: green;font-size:18px"> Battery Tests </p>
Another cool feature of the Artemis board is its onboard battery charger. When the LiPo battery is connected to the board while plugged into a laptop via USB-C, the board is able to charge the battery (indicated by the yellow light in the image below). When the board is disconnected from the computer, it is able to source power from the battery; this can be seen in the video below, in which the board turns on the blue built in LED when it detects a tone being whistled. The board determines that a tone is being whistled by identifying the loudest frequency using the microphone, just as was done above; if the pitch was above a certain threshold frequency value, then the light would turn on (this frequency value was determined via trial and error - speaking is at much lower tones than whistling)<br>
<b>Code:</b><br>
```C
if(ui32LoudestFrequency >= 500){digitalWrite(LED_BUILTIN,HIGH);}
  else{digitalWrite(LED_BUILTIN,LOW);}
```
<i>The battery being charged while the board is connected to my laptop</i>
<img src="lipo.jpg" alt="Battery"><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/MvvlOql-GQY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br> <br>

<Center> <h1> Lab 2 </h1>
    <h2> <i> Bluetooth Communication </i></h2> </Center>

<h3 style="color: green;"> Setup </h3>
I had a little trouble setting up the bluetooth on the provided ECE4960 Ubuntu VM, so I just opted to use my windows machine for the entirety of this lab. To enable bluetooth communication with the Artemis board, I installed the necessary python library (bleak) using pip. I also downloaded the provided distribution code (python scripts and Arduino IDE code) as a starting point for this lab.<br>
Once the necessary libraries were installed, I ran the example code to see if my laptop was able to connect to the Artemis board via bluetooth. Luckily, I was able to connect the two after a few tries and added the board's MAC address to the settings cache.

<h3 style="color: green;"> Pinging the Robot </h3>
Each ping packet is 99 bytes - one length, one command, 96 data bytes, and one extra.To measure the round trip response times and flucutuations in latency, I modified the PONG case as below:
```Python
timeDiff = time.time() - theRobot.now
instantDat.append(round(timeDiff,5))
if(Settings["pingLoop"]):
    loop.create_task(theRobot.ping())
```
The program records the time difference between pongs and records it in a python list. When the python script is killed by the user, these python lists are converted to NumPy arrays before the program quits out (this was done because appending to lists is computationally faster than appending to NumPy arrays and I wanted to skew the measurement as little as possible). While a slightly more accurate average may be acquired by only measuring the time every few pings, capturing the round trip time of every ping only adds a few extra commands; since python per-line execution times are on the order of microseconds, this shouldn't skew the data a whole lot - collecting more data points may also give a better idea of the variation in latency. The data I collected was then used to make the following histogram of round trip times: <br>
<img src="reg_histo.png" alt="Regular RT Histogram"><br>
The average round-trip ping time was 0.1185 seconds with a standard deviation of 0.0095 seconds with a total of 500 datapoints collected. Interestingly, the data seems to be bimodal in a sense - the majority of times are centered around ~.1125 seconds, but there's a second significant cluster at around 0.13 seconds. 
This test was performed with the artemis board right next to my laptop. To see how the round-trip time varies with distance, I left the board on my porch and pinged it with my laptop from across the street - results can be seen below: <br>
<img src="dist_histo.png" alt="Distance RT Histogram"><br> 
The average RT ping time in this case was 0.145 seconds with a standard deviation of 0.034 seconds, also with 500 datapoints collected. As with the last trial, the data also seems to be bimodal in a sense (although it's shifted right and a bit less apparent), but the distribution is a fair bit smoother than in the previous. I was suprised to see that the difference in average RT time did not differ by such a large margin (only about ~0.03 sec slower on average from a distance). <br>
While these rates are not particularly slow, they are significantly slower than a wired serial connection. The standard baud rate (roughly the number of bits/sec) that we've been using for the Artemis board is 115200 - this translates to about 11520 Bytes/sec when accounting for start/stop bits in transmission. Since each byte would have to travel back and forth, this implies that 11520/2=5760 bytes could be transmitted back and forth per second. Since our average RT time over bluetooth was just over 0.1 seconds for 99 bytes, this means that the (somewhat idealized) wired connection is approximately 5-6 times faster than Bluetooth.

<h3 style="color: green;"> Requesting a float </h3>
While pinging the robot is pretty cool and serves as a quick check to see if the bluetooth link is functional, sending and receiving meaningful data to/from the Artemis board is much more useful. As a first attempt to transmit values between the two nodes, I tried requesting a float from the board via a command sent by my laptop. Upon reception of this REQ_FLOAT command, the board sends back a packet that contains a 4-byte float value; this return command struct also contains a length field and a command value that the computer uses upon reception of this retun packet. <br>
In order to write a float value into the data bytearray, I ended up casting the data pointer into a float pointer, then storing the desired value in there: <br>
```C
res_cmd->length = sizeof(float);
res_cmd->command_type = GIVE_FLOAT;
*((float*)res_cmd->data) = putVal;
amdtpsSendData((uint8_t *)res_cmd, 6);
```
When testing the program, I first tried transmitting pi over Bluetooth by casting the math library's M_PI constant to a float and sending that, but the received value wasn't exactly pi. To determine if that error was due to an imprecise M_PI constant or floating point isses, I just decided to send the number 3.14 as a float instead; rather than receiving exactly 3.14, the Python code unpacked that value as 3.140000104904175, indicating that there are some issues with floating point comparison/conversion. These issues in C are fairly well known, but one must still be really careful when comparing two float values (especially with subtraction).

<h3 style="color: green;"> Testing the Data Rate </h3>
The procedure for sending two numbers was very similar to sending a float - the only difference was the number of bytes and that they had to be inserted into different points int the array. 
```C
//ct declared as a global uint32_t, lastTime declared as global uint64_t 
lastTime = (uint64_t)micros();
memcpy((uint32_t*)&res_cmd->data[0],&ct,4);
memcpy((uint64_t*)&res_cmd->data[4],&lastTime,8);
amdtpsSendData((uint8_t *)res_cmd, 14);
```
With 5000 received packets, a total of 881 were lost (1 packet dropped for every 5.7 sent, on average). The datastream rate was also much faster, with an average time of 0.0128 seconds between packets received. Below is a histogram of the packet RT times: <br>
<img src="bt_histo.png" alt="Regular Bytestream RT Histogram"><br>

I also tried the same thing but with sending 4x the amount of data in a packet (4-32 bit ints, 4-int_64's). With 5000 received packets, a total of 890 were lost and the average time between packets was also 0.0128 secs - it seems like the amount of data transferred in a single packet has no significant effect on the bytestream performance; this makes sense since all 99 bytes are transmitted each time anyway. The histograms look shockingly similar to each other: <br>
<img src="bt_4x_hist.png" alt="Regular Bytestream RT Histogram"><br>

<h3 style="color: green;"> Command Framework Modifications </h3>
To expand on the command framework, I added a command that transmits 9 floats as provided by the IMU (should be convenient later). I also added some commands to transfer larger PNG files (described below). To do this I had to modify both constants.py and commands.h


<h3 style="color: green;"> 2+ KB File Transfer</h3>
Unfortunately, I did not have enough time to fully complete this optional part of the lab (somehow prelims are starting already!). However, my original idea was to bounce a PNG image bytearray between the two devices and see how the final image looked. To do this, I expanded the framework to include PNG_START_TRANSMIT and PNG_IMG commands that indicated when a file transfer starts and was in progress. Because the full file would have to be distributed across multiple packets, the cmd->length would be the packet number, and the file size would be indicated by the START_TRANSMIT command.
```C
case PNG_IMG_START:{
  pngSize = cmd->length;
  Serial.print("PNG Size is ");
  Serial.println(pngSize);
}
case PNG_IMG:{
  int countt = cmd->length;
  *((uint8_t*)&img[countt*96]) = *cmd->data;
}
```
