.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _tilt_uno:

Lesson 5 Tilt Switch
=========================

Introduction
--------------------

The tilt switch used here is a ball one with a metal ball inside. It is
used to detect inclinations of a small angle.

Components
--------------

.. image:: img/uno07.png
    :align: center


* :ref:`SunFounder R3 Board`
* :ref:`Breadboard`
* :ref:`Jumper Wires`
* :ref:`Tilt Switch`


Schematic Diagram
---------------------

.. image:: img/image76.png


Experimental Procedures
-----------------------------

**Step 1:** Build the circuit.

.. image:: img/image77.png


**Step 2:** Open the code file.

**Step 3:** Select the **Board** and **Port.**

**Step 4:** Upload the sketch to the board.

Now, tilt the switch, and the LED attached to pin 13 on Uno board will
light up.

.. image:: img/image78.jpeg


Code
--------

.. raw:: html

   <iframe src=https://create.arduino.cc/editor/sunfounder01/b836688d-452c-4c43-a5d3-d8cc6c163b2a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Code Analysis
----------------------

**Code Analysis 7-1 Whole Code**

.. code-block:: arduino

    const int ledPin = 13; //the led attach to

    void setup()

    {

      pinMode(ledPin,OUTPUT); //initialize the ledPin as an output

      pinMode(2,INPUT); //set pin2 as INPUT

      digitalWrite(2, HIGH); //set pin2 as HIGH

    }

    /******************************************/

    void loop()

    {

      int digitalVal = digitalRead(2); //Read the value of pin2

      if(HIGH == digitalVal) //if tilt switch is not breakover

      {

         digitalWrite(ledPin,LOW); //turn the led off

      }

      else //if tilt switch breakover

      {

         digitalWrite(ledPin,HIGH); //turn the led on

      }

    }

The whole code are very simple, one pin of the tilt switch is connected
to pin2, another pin is connected to GND, when tilt the switch, the two
pins of the switch will be connected to GND, then let the LED on the
pin13 lights up.