[
    {
        "id": "4026e3d9.df925c",
        "type": "tab",
        "label": "Flow 6",
        "disabled": false,
        "info": ""
    },
    {
        "id": "ef08b2ba.71eb",
        "type": "http in",
        "z": "4026e3d9.df925c",
        "name": "setgpio5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 170,
        "y": 140,
        "wires": [
            [
                "9f87b01f.944fd",
                "e775cfa4.2231a"
            ]
        ]
    },
    {
        "id": "9f87b01f.944fd",
        "type": "function",
        "z": "4026e3d9.df925c",
        "name": "set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 180,
        "wires": [
            [
                "8f28f9f2.abc2c8"
            ]
        ]
    },
    {
        "id": "8f28f9f2.abc2c8",
        "type": "rpi-gpio out",
        "z": "4026e3d9.df925c",
        "name": "",
        "pin": "7",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 430,
        "y": 500,
        "wires": []
    },
    {
        "id": "e775cfa4.2231a",
        "type": "function",
        "z": "4026e3d9.df925c",
        "name": "return to status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 320,
        "wires": [
            [
                "e5469422.707538",
                "81448ac9.64aed8"
            ]
        ]
    },
    {
        "id": "e5469422.707538",
        "type": "http response",
        "z": "4026e3d9.df925c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 600,
        "y": 320,
        "wires": []
    },
    {
        "id": "81448ac9.64aed8",
        "type": "debug",
        "z": "4026e3d9.df925c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 620,
        "y": 440,
        "wires": []
    },
    {
        "id": "87b24e04.e7596",
        "type": "http in",
        "z": "4026e3d9.df925c",
        "name": "cleargpio5",
        "url": "/cleargpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 100,
        "y": 600,
        "wires": [
            [
                "c2394044.a2377",
                "ad230009.e084f"
            ]
        ]
    },
    {
        "id": "c2394044.a2377",
        "type": "function",
        "z": "4026e3d9.df925c",
        "name": "clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 600,
        "wires": [
            [
                "8f28f9f2.abc2c8"
            ]
        ]
    },
    {
        "id": "ad230009.e084f",
        "type": "function",
        "z": "4026e3d9.df925c",
        "name": "return to status",
        "func": "msg.payload = \"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 700,
        "wires": [
            [
                "e5469422.707538",
                "81448ac9.64aed8"
            ]
        ]
    }
]
