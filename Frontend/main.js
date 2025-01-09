$(document).ready(function () {
    // Welcome text aninmation
    $('.welcome-text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });

    // ReadOut text aninmation
    $('.readOut-caption').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
            sequence: true,
        },
        out:{
            effect: "bounceOut",
            sequence: true,
        },
    });

    // Initialising speech waves
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200, 
        style: "ios9",
        amplitude: "1",
        speed: "0.3",
        autostart: true
      });
});