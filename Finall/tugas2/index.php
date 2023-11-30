<?php

include "Classes/Mammal.php";
include "Classes/Bird.php";

use Zoo\Mamalia;
use Zoo\Bird;

$mammal = new Mamalia("Singa", 5, "Makan");
echo displayOutput($mammal);

$bird = new Bird("Burung Kakatua", 2, "Warna Unik");
echo displayOutput($bird);

function displayOutput($animal)
{
    $output = "<div style='border: 2px solid #333; padding: 10px; margin-bottom: 10px;'>";
    $output .= "<strong>{$animal->summonSpirit()}</strong>";
    $output .= "</div>";

    return $output;
}