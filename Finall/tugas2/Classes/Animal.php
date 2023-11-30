<?php

namespace Zoo;

abstract class Animal
{
    protected $name;
    protected $age;

    abstract public function summonSpirit();

    public function __construct($name, $age)
    {
        $this->name = $name;
        $this->age = $age;
    }
}