function getBiggestNumberInArray(nums1,nums2){
    let biggestnum1 = 0
    let biggestnum2 = 0
    for (i in nums1){
        if(nums1[i]> 0){biggestnum1 = nums1[i]}
    }
    for (i in nums2){
        if(nums2[i]>0){biggestnum2 = nums2[i]}
    
    }
    if (biggestnum1>=biggestnum2){
    return (biggestnum1)}
    else{return(biggestnum2)}
}

const nu1 = [1,2,3,45]
const nu2 = [1,4,5,8,9,40]

console.log(getBiggestNumberInArray(nu1,nu2))