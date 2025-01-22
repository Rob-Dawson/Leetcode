// const nums = [-10, 10, 10, 10];
// const nums = [-4, -2, 1, 4, 8];
// const nums = [-1, 1];
// const nums = [2, 1, 1, -1, 100000];
let closest = nums[0];
nums.forEach((num) => {
  if (Math.abs(num) < Math.abs(closest)) {
    closest = num;
  }
  if (Math.abs(num) === Math.abs(closest)) {
    if (num > closest) {
      closest = num;
    }
  }
});

console.log(closest);
