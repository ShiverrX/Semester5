<?php

namespace Zoo;

include "Animal.php";
include "Traits/Greet.php";

class Mamalia extends Animal
{
    use Greet;

    private $specialAbility;

    public function __construct($name, $age, $specialAbility)
    {
        parent::__construct($name, $age);
        $this->specialAbility = $specialAbility;
    }

    public function summonSpirit()
    {
        return $this->greet() . "Saya adalah mamalia bernama $this->name, berusia $this->age tahun, dan kemampuan khusus saya adalah $this->specialAbility.";
    }
}
