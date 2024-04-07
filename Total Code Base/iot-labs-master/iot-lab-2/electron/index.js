console.log("hello")
document.onkeydown = updateKey;
document.onkeyup = resetKey;

function client(){
    var server_port = 65432;
    var server_addr = "192.168.0.176"; // the IP address of your Raspberry PI
    const net = require('net');
    var input = document.getElementById("message").value;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}\r\n`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        document.getElementById("bluetooth").innerHTML = data;
        console.log(data.toString());
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}

function arrow_pressed(btn) {
    console.log(btn)
    var server_port = 65432;
    var server_addr = "192.168.0.176"; // the IP address of your Raspberry PI
    const net = require('net');

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${btn}`);
    });
    
    
    // get the data from the server
    client.on('data', (data) => {
        let direct_span = document.getElementById("direction")
        res = data.toString().split(',')
        console.log(res)
        direction_ = res[0]
        power = res[1]
        temp = res[2]
        if(direction_ == 'f') {
            direct_span.innerHTML = "Forwards";
        } else if(direction_ == 'r') {
            direct_span.innerHTML = "Right";
        } else if(direction_ == 'l') {
            direct_span.innerHTML = "Left";
        } else {
            direct_span.innerHTML = "Backwards";
        }
        document.getElementById('power').innerHTML = power;
        document.getElementById('temperature').innerHTML = temp;
        client.end();
        client.destroy();
    });
    
    client.on('end', () => {
        console.log('disconnected from server');
    });

}
/*
// for detecting which key is been pressed w,a,s,d
function updateKey(e) {

    e = e || window.event;

    if (e.keyCode == '87') {
        // up (w)
        document.getElementById("upArrow").style.color = "green";
        send_data("87");
    }
    else if (e.keyCode == '83') {
        // down (s)
        document.getElementById("downArrow").style.color = "green";
        send_data("83");
    }
    else if (e.keyCode == '65') {
        // left (a)
        document.getElementById("leftArrow").style.color = "green";
        send_data("65");
    }
    else if (e.keyCode == '68') {
        // right (d)
        document.getElementById("rightArrow").style.color = "green";
        send_data("68");
    }
}
*/
// reset the key to the start state 
function resetKey(e) {

    e = e || window.event;

    document.getElementById("upArrow").style.color = "grey";
    document.getElementById("downArrow").style.color = "grey";
    document.getElementById("leftArrow").style.color = "grey";
    document.getElementById("rightArrow").style.color = "grey";
}


// update data for every 50ms
function update_data(){
    setInterval(function(){
        // get image from python server
        client();
    }, 50);
}
