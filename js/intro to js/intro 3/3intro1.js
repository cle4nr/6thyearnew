function canDriveCar(user,car){
    if (user['age'] >= 18){var correctage = true}
    else {var correctage = false}

    if (car['engineSize'] <= 1000){var correctcc = true}
    else {var correctcc = false}

    if (correctage && correctcc == true) {console.log('you can drive')}
    else {console.log('you cannot drive')}

}
let user1 = {'name':'Jon Doe','age':21}
let car1 = {'engineSize':1200,'name':'Mazda 3'}
canDriveCar(user1,car1)

function areAllNumbersEven(numbers){
    let evenamt = 0
    for (i in numbers){
        if (numbers[i]%2==0){evenamt++}} //need to do numbers[i] because js auto uses index
    if (evenamt == numbers.length){console.log('even')}
    else {console.log('not all are even')}
    
}

const nums = [2,4,6,8]
areAllNumbersEven(nums)

function getBiggestNumberInArrays(numbers1,numbers2){
let big1 = 0
let big2 = 0
for (i in numbers1){
    if (numbers1[i]>0){big1 = numbers1[i]}
    if (numbers1[i]>big1){big1 = numbers1[i]}

}
for (i in numbers2){
    if (numbers2[i]>0){big2 = numbers2[i]}
    if (numbers2[i]>big2){big2 = numbers2[i]}

}
if(big1>=big2){console.log(big1)}
else(console.log(big2))

}
const nums1 = [2,4,6,8]
const nums2 = [2,3,8,9]
getBiggestNumberInArrays(nums1,nums2)