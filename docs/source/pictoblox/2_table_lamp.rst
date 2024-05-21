.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

2. Table Lamp
================

The last project was to make the built-in LED on the Arduino board light up. Here, we connect an LED on the breadboard and have the sprite control the blinking of this LED.

When the Button sprite on the stage is clicked, the LED will blink 5 times and then stop.

.. image:: img/2_button.png

You Will Learn
---------------------


- Breadboard, LEDs and Resistors
- Building a circuit on a breadboard
- Delete and select sprites
- Switching costumes
- Set a limited number of repeat loops

Build the Circuit
-----------------------

Follow the diagram below to build the circuit on the breadboard.

Since the anode of the LED (the longer pin) is connected to pin 9 through a 220Ω resistor, and the cathode of the LED is connected to GND, you can light up the LED by giving pin 9 a high level.

.. image:: img/2_circuit.png

* :ref:`Breadboard`
* :ref:`LED`
* :ref:`Resistor`

Programming
------------------
The whole programming is divided into 3 parts, the first part is to select the desired sprite, the second part is to switch the costume for the sprite to make it look clickable, and the third part is to make the LED blink.

**1. Select Button3 sprite**

Delete the existing Tobi sprite by using the Delete button in the upper right corner, and select a sprite again.

.. image:: img/2_tobi.png

Here, we select the **Button3** sprite.

.. image:: img/2_button3.png

Click on Costumes in the top right corner and you will see that the Button3 sprite has 2 costumes, we set **button3-a** to be released and **button3-b** to be pressed.

.. image:: img/2_button3_2.png

**2. Switching costumes**.

When the sprite is clicked (**Events** palette), it switches to costume for **button3-b** (**looks** palette).

.. image:: img/2_switch.png

**3. Make the LED blink 5 times**

Use the [Repeat] block to make the LED blink 5 times (High-> LOW cycle), remember to change pin 13 to pin 9, and finally switch the costume back to **button3-a**.

* [Repeat 10]: limited number of repeat loops, you can set the number of repeats yourself, from the **Control** palette.

.. image:: img/2_led_on_off.png




