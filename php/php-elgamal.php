<?php

class elgamal
{

    var $x;
    var $p;
    var $g;
    var $y;
    var $text;
    function isPrime($number)
    {
        // 1 is not prime
        if ($number == 1) {
            return false;
        }
        // 2 is the only even prime number
        if ($number == 2) {
            return true;
        }
        // square root algorithm speeds up testing of bigger prime numbers
        $x = sqrt($number);
        $x = floor($x);
        for ($i = 2; $i <= $x; ++$i) {
            if ($number % $i == 0) {
                break;
            }
        }

        if ($x == $i - 1) {
            return true;
        } else {
            return false;
        }
    }

    function getKey()
    {
        //get public
        if (!$this->isPrime($this->p)) {
            echo "[+] Pastikan kolom bilangan prima adalah bilangan prima\n";
            exit("keluar");
        }
        return  bcpowmod($this->g, $this->x, $this->p);
    }

    function pecahString()
    {
        // plit text into array
        return str_split($this->text);
    }
    function getAscii()
    {
        foreach ($this->pecahString() as $pecahan) {
            $ascii[] = ord($pecahan);
        }
        return $ascii;
    }
    function encrypt()
    {
        //merge delta and gamma into array every m
        foreach ($this->getAscii() as $m) {
            $k = $this->getK($m);
            $cipher[] = bcpowmod($this->g, $k, $this->p); //gamma
            $cipher[] = bcmod(bcmul(bcpow($this->getKey(), $k), $m), $this->p); //delta
        }
        return $cipher;
    }

    function decrypt()
    {
        $cipher = $this->cipher;
        for ($i = 0; $i < count($cipher); $i++) {
            if ($i % 2 != 0) {
                $delta[] = $cipher[$i]; //indeks odd
            } else {
                $gamma[] = $cipher[$i]; // indeks even
            }
        }
        $pangkat = $this->p - 1 - $this->x;
        for ($i = 0; $i < count($gamma); $i++) {

            $xxxx[] = chr(bcmod(bcmul($delta[$i], bcpow($gamma[$i], $pangkat)), $this->p));
        }

        return implode('', $xxxx);
    }
    function getK()
    {
        return rand(1, ($this->p - 2)); //random number
    }
}
