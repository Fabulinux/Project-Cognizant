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

function migratoryBirds(n, ar) {
    // Complete this function
    let birdCount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0};
    let mostFrequentBird = 0;
    let currentMaxBirdCount = 0;
    
    for (var i = 0; i<ar.length; i++){
        birdCount[ar[i]]++;
        
        // if frequency of current bird is greater than current max update max count and bird
        if(birdCount[ar[i]] > currentMaxBirdCount){
            currentMaxBirdCount = birdCount[ar[i]];
            mostFrequentBird = ar[i];
        }
        // if equal, get the smaller bird, no need to update currentMaxBirdCount
        else if(birdCount[ar[i]] === currentMaxBirdCount){
            mostFrequentBird = (ar[i] < mostFrequentBird) ? ar[i] : mostFrequentBird;
        }
    }
    return mostFrequentBird;
}

function main() {
    var n = parseInt(readLine());
    ar = readLine().split(' ');
    ar = ar.map(Number);
    var result = migratoryBirds(n, ar);
    process.stdout.write("" + result + "\n");

}
