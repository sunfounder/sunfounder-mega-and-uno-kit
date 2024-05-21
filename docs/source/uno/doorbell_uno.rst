.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _doorbell_uno:

Lesson 4 Doorbell
=========================

Introduction
-----------------

A buzzer is a great tool in your experiments whenever you want to make
some sounds. In this lesson, we will learn how to drive an active buzzer
to build a simple doorbell.

Components
---------------

.. image:: img/uno06.png
    :align: center


* :ref:`SunFounder R3 Board`
* :ref:`Breadboard`
* :ref:`Jumper Wires`
* :ref:`Resistor`
* :ref:`Capacitor`
* :ref:`Button`
* :ref:`Buzzer`

Schematic Diagram
-----------------------

.. image:: img/image71.png
   :align: center
   


Experimental Procedures
-------------------------

**Step 1:** Build the circuit (Long pins of buzzer is the Anode and the
short pin is Cathode).

.. image:: img/image72.png
    :align: center


**Step 2:** Open the code file.

**Step 3:** Select the **Board** and **Port.**

**Step 4:** Upload the sketch to the board.

Now, you should hear the buzzer beep.

.. image:: img/image73.jpeg
   :align: center


Code
--------

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/4a3bfe94-a3bb-4b0c-afe6-9e740f470dc4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Code Analysis
-----------------

**Define variables**

.. code-block:: arduino

    const int buttonPin = 2; //the button connect to pin2

    const int buzzerPin = 8; //the led connect to pin8

    /**********************************/

    int buttonState = 0; //variable for reading the pushbutton status

Connect the button to pin 2 and buzzer to pin 8. Define a variable
``buttonState`` to restore the state of the button.

**Set the input and output status of the pins**

.. code-block:: arduino

    void setup()

    {

        pinMode(buttonPin, INPUT); //initialize the buttonPin as input

        pinMode(buzzerPin, OUTPUT); //initialize the buzzerpin as output

    }

We need to know the status of the button in this experiment, so here set
the ``buttonPin`` as INPUT; to set HIGH/LOW of the buzzer, we set
``buzzerPin`` as OUTPUT.

**Read the status of the button**

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);

buttonPin(Pin2) is a digital pin; here is to read the value of the
button and store it in ``buttonState``.

**digitalRead (Pin)**: Reads the value from a specified digital pin,
either HIGH or LOW.

**Press the button to make the buzzer sound**

.. code-block:: Arduino

    if (buttonState == HIGH ) //When press the button, run the following code.
    { 
        for (i = 0; i < 50; i++) 
        /*When i=o, which accords with the condition i<=50, i++ equals to 1 
        (here in i = i + 1, the two "i"s are not the same, but i(now） = i（before） + 1). 
        Run the code in the curly braces: let the buzzer beep for 3ms and stop for 3ms. 
        Then repeat 50 times.*/

        { 
            digitalWrite(buzzerPin, HIGH); //Let the buzzer beep.
            delay(3); //wait for 3ms
            digitalWrite(buzzerPin, LOW); //Stop the buzzer.
            delay(3); //wait for 3ms 
        }

        for (i = 0; i < 80; i++) //Let the buzzer beep for 5ms and stop for 5ms, repeat 80 times.
        { 
            digitalWrite(buzzerPin, HIGH);
            delay(5); //wait for 5ms
            digitalWrite(buzzerPin, LOW);
            delay(5); //wait for 5ms 
        }
    }

In this part, when the **buttonState** is High level, then let the
buzzer beeping in different frequency which can simulate the doorbell.