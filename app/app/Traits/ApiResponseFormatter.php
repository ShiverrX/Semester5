<?php

namespace app\Traits;

// UNTUK FORMATTING RESPONSE 
trait ApiResponseFormatter
{
    public function apiResponse($code = 200, $message = "success", $data = [])
    {
        // DARI PARAMETER AKAN DI FORMATI MENJADI SEPERI DI BAWAH INI
        return json_encode([
            "code" => $code,
            "message" => $message,
            "data" => $data,
        ]);
    }
}
