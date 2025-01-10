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
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync: true,
        },
    });

    // Initialising speech waves
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 0,
        height: 200, 
        style: "ios9",
        amplitude: "1",
        speed: "0.3",
        autostart: true
      }); 

    //   Clicking the mic button
    $("#MicBtn").click(function () {
        $("#oval").removeClass("fade-in").addClass("fade-out");
        $("#SiriWave").removeClass("hidden").addClass("fade-in");
    
        // Toggle hidden attributes after transition
        setTimeout(function () {
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
    
            // Initialize SiriWave after making the container visible
            var siriWave = new SiriWave({
                container: document.getElementById("siri-container"),
                width: 750, 
                height: 200,
                style: "ios9",
                amplitude: 1,
                speed: 0.3,
                autostart: true
            });
        }, 500);
    });
});