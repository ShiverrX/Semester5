<?php

function generator($n)
{   
    $output = "";

    for ($i = 1; $i <= $n; $i++) {
        if($i %3 == 0){$output .= "Hello";}
        if($i %5 == 0){$output .= "World";}

        if($output == ""){$output =$i;}
        echo "$output\n";
        $output = "";
    }
}

generator(15);