.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

8. Tumbler
=============

Now we use a tilt switch to control tumbler on the stage, so that the switch tilted, tumbler also tilted.

.. Image:: img/8_tumbler.png

You Will Learn
---------------------

- How the tilt switch works
- [`if then else <https://en.scratch-wiki.info/wiki/If_()_Then,_Else_(block)#:~:text=The%20if%20()%20then%2C%20else,the%20second%20C%20 20will%20activate.>`_] block
- Adding external sprite

Build the circuit
-----------------------

The tilt switch used here is a ball with a metal ball inside. When it is upright, the 2 pins are connected together, and when it is tilted, they are separate.

Build the circuit according to the following diagram:

* Connect one pin of the tilt switch to pin 12, which is connected to a pull-down resistor and a 0.1uF (104) capacitor (used to eliminate jitter and output a stable level when the tilt switch is operating).
* Connect the other end of the resistor and capacitor to GND and the other pin of the tilt switch to 5V.

.. image:: img/8_circuit.png

* :ref:`Breadboard`
* :ref:`Tilt Switch`
* :ref:`Resistor`
* :ref:`Capacitor`

Programming
------------------

**1. Customize the sprite**

Select the **Tobi** sprite and go to the **Costumes** page. Select the icon in the bottom left corner and then select **Upload Costume**.

.. image:: img/8_upload.png

Then open ``tumbler1.png`` and ``tumbler2.png`` in the ``sunfounder-uno-and-mega-kit\scratch\picture`` path and make sure you have downloaded the relevant material.
.. image:: img/8_add_tumbler.png

Remove the **Tobi** sprite related costume and change the name to **Tumbler**. Now that we have customized a new sprite Tumbler, we start scripting it.

.. image:: img/8_rename.png

**2. Tilt the switch**

If the value of pin12 is read as 0 (the switch is tilted), switch the sprite costume to **tumbler2**, which is also in the tilted state. Otherwise, switch the sprite costume to **tumbler1**, upright.

* [`if then else <https://en.scratch-wiki.info/wiki/If_()_Then,_Else_(block)#:~:text=The%20if%20()%20then%2C%20else,the%20second%20C%20 20will%20activate.>`_]: The block checks its boolean condition; if the condition is true, the code held inside the first C (space) will activate; if the if the condition is false, the code inside the second C will activate.
* [=]: The block is used to compare the equality of the values on the 2 sides of the equal sign, from the **Operators** platette.

.. image:: img/8_script.png