/**
 * @param {number[]} nums
 * @return {boolean}
 */
var circularArrayLoop = function(nums) {
  var pos = 0;
  var prevPos;
  var i = 0;
  var direction = (nums[0] > 0) ? 1 : -1;
  var currDirection;

  // Only need to go through the array once, if no loop then no loop will be found
  for (var j = 0; j<nums.length;j++){

    // Gets the value and adds it to get the step towards next location
    i = i + parseInt(nums[i]);

    // Direction flag to ensure going in the right location
    currDirection = (nums[i] > 0) ? 1 : -1;
      
    // If outside of bounds, get value that wraps, preserve currDirection
    if(i < 0){
      i = nums.length + i;
      currDirection = -1;
    }
    if(i>=nums.length){
      i = i - nums.length;
      currDirection = 1;
    }
      
      // If its been checked and there is a previous spot checked and its not the same spot then its valid
      // Since it will be a loop of > 1
    if(nums[i].toString().includes('checked') &&(prevPos!== 'undefined') && (prevPos !== pos)){
      return true;
    }
    // if landed in the same spot, increment the spot so it goes through the list again.
    else if(prevPos === pos){
      prevPos = 'undefined';
      i++;

      if(i>=nums.length){ // If at the right edge then wrap around
        i = i - nums.length;

      }
      pos = i;
      j--; // Decrement to account for reset
      direction = (nums[i] > 0) ? 1 : -1;
      currDirection = direction; // reset direction 
    }
    
    else{
        // Check flag
      nums[pos] = nums[pos].toString() + 'checked';
      prevPos = pos; // sets the previous position
      pos = i;// gets the current position to use


    }
      
      // if direction swap then error out
    if(direction !== currDirection){
      return false;
    }
  }
  return false;
};

