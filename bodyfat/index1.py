# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:15:26 2022

@author: Prajjwal
"""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <div style="color:blue">
        <form action="{{ url_for('predict')}}" method="POST">
            <h2>Predictive analysis</h2>
            <h3>weight</h3><input id="first" name="weight"  type="number">
            <h3>height</h3><br><input id="second" name="height" type="number">
            <h3>neck</h3><input id="third" name="neck"  type="number">
            <h3>chest</h3><br><input id="fourth" name="chest"  type="number">
            <h3>abdomen</h3><br><input id="fifth" name="abdomen"  type="number">
            <h3>hip</h3><br><input id="sixth" name="hip"  type="number">
            <h3>thigh</h3><br><input id="seventh" name="thigh"  type="number">
            <h3>knee</h3><br><input id="eighth" name="knee"  type="number">
            <h3>ankle</h3><br><input id="ninth" name="ankle"  type="number"> 
            <h3>bicep</h3><br><input id="tenth" name="bicep"  type="number">
            <h3>forearm</h3><br><input id="eleventh" name="forearm"  type="number">
            <h3>wrist</h3><br><input id="twelfth" name="wrist"  type="number">
                
            </select>
            <br><br><button id="sub" type="submit ">Predict body fat percentage</button>
            <br>

          <br><br><h3>{{ prediction_text }}<h3>


        </form>



        <br><br><h3>{{ prediction_text }}<h3>
    </div>




    <style>
        body {
            background-color: lightslategray;
            text-align: center;
            padding: 0px;
        }
        
        #research {
            font-size: 18px;
            width: 100px;
            height: 23px;
            top: 23px;
        }
        
        #box {
            border-radius: 60px;
            border-color: 45px;
            border-style: solid;
            font-family: cursive;
            text-align: center;
            background-color: rgb(168, 131, 61);
            font-size: medium;
            position: absolute;
            width: 700px;
            bottom: 9%;
            height: 850px;
            right: 30%;
            padding: 0px;
            margin: 0px;
            font-size: 14px;
        }
        
        #fuel {
            width: 83px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 20px;
        }
        
        #fuel:hover {
            background-color: coral;
        }
        
        #research {
            width: 99px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 18px;
        }
        
        #research:hover {
            background-color: coral;
        }
        
        #resea {
            width: 99px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 18px;
        }
        
        #resea:hover {
            background-color: coral;
        }
        
        #sub {
            width: 120px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 18px;
        }
        
        #sub:hover {
            background-color: darkcyan;
        }
        
        #first {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #second {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #third {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #fourth {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
    </style>
</body>

</html>

