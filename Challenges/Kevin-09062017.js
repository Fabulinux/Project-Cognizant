process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function getTotalX(a, b) {
    var leftRange  = a.reduce(function(a, b) {
    return Math.max(a, b);
});;
    var rightRange  = b.reduce(function(a, b) {
    return Math.min(a, b);
});;
    var list = 0;
    var check = true;
    for(var i =leftRange; i<= rightRange; i++){
        for(var j=0; j<a.length;j++){
            if(i % a[j] !== 0){
                check = false;
            }
            
        }
        for(var k=0;k<b.length;k++){
            if(b[k] % i !== 0){
                 check = false; 
            }
                
        }
                   
                   
        if(check){
           list++;      
        }
        else{
            check = true;
        }
    }
    return list;
}



function main() {
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var m = parseInt(n_temp[1]);
    a = readLine().split(' ');
    a = a.map(Number);
    b = readLine().split(' ');
    b = b.map(Number);
    var total = getTotalX(a, b);
    process.stdout.write("" + total + "\n");

}
