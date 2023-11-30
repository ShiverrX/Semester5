<?php

namespace Zoo;

class Bird extends Animal
{
    use Greet;

    private $featherColor;

    public function __construct($name, $age, $featherColor)
    {
        parent::__construct($name, $age);
        $this->featherColor = $featherColor;
    }

    public function summonSpirit()
    {
        return $this->greet() . "Saya adalah burung bernama $this->name, berusia $this->age tahun, dan warna bulu saya adalah $this->featherColor.";
    }
}
