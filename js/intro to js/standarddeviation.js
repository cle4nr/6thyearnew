const nums = [20,21,19,22,21,20,19,20,21,20]
let lennums = nums.length
let sum = 0
for (let i = 0; i < lennums;i++){
    sum += nums[i] 
}
let mean = sum / lennums
console.log(mean)