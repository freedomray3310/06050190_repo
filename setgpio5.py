[
    {
        "id": "6fb44109.e8f66",
        "type": "tab",
        "label": "Flow 4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "59041cdf.6b7224",
        "type": "http in",
        "z": "6fb44109.e8f66",
        "name": "",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 160,
        "wires": [
            [
                "4c5cb8df.376988",
                "8bc68faa.79862"
            ]
        ]
    },
    {
        "id": "8bc68faa.79862",
        "type": "function",
        "z": "6fb44109.e8f66",
        "name": "set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 180,
        "wires": [
            [
                "3bdb2e2f.171d72"
            ]
        ]
    },
    {
        "id": "3bdb2e2f.171d72",
        "type": "rpi-gpio out",
        "z": "6fb44109.e8f66",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 660,
        "y": 120,
        "wires": []
    },
    {
        "id": "4c5cb8df.376988",
        "type": "function",
        "z": "6fb44109.e8f66",
        "name": "return ",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 420,
        "y": 320,
        "wires": [
            [
                "5b2073e4.3263ec",
                "4f81fde6.475904"
            ]
        ]
    },
    {
        "id": "5b2073e4.3263ec",
        "type": "http response",
        "z": "6fb44109.e8f66",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 710,
        "y": 260,
        "wires": []
    },
    {
        "id": "4f81fde6.475904",
        "type": "debug",
        "z": "6fb44109.e8f66",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 680,
        "y": 360,
        "wires": []
    }
]
