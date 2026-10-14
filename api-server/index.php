<?php

require_once __DIR__ . '/vendor/autoload.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;

$request = Request::createFromGlobals();
$path = $request->getPathInfo();
$method = $request->getMethod();


if ($method === 'GET' && ($path === '/' || $path === '/api/cars')) {
    $filePath = __DIR__ . '/data.json';

    if (!file_exists($filePath)) {
        $response = new JsonResponse(
            ['error' => 'Файл data.json не знайдено'],
            Response::HTTP_INTERNAL_SERVER_ERROR
        );
    } else {
        $jsonContent = file_get_contents($filePath);

        $response = JsonResponse::fromJsonString($jsonContent, Response::HTTP_OK);
    }
} else {
    $response = new JsonResponse(
        ['error' => 'Маршрут не знайдено. Використовуйте GET / або GET /api/cars'],
        Response::HTTP_NOT_FOUND
    );
}

$response->send();