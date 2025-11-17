/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */



var mergeOld = function(nums1, m, nums2, n) {

    //minha solução inicial, que funciona, mas não é eficiente
    if (!n == 0 ){
        for (let i = 0; i < n; i++){
            nums1[i+m] = nums2[i];
        }
        
    
        nums1.sort((a, b) => a - b); // complexidade média é O(n log n)
        
    };

}



var merge = function(nums1, m, nums2, n) {

    // solução eficiente do gpt

    let i = m - 1;         // último elemento válido de nums1
    let j = n - 1;         // último elemento de nums2
    let k = m + n - 1;     // última posição disponível em nums1

    // Enquanto ainda houver elementos em nums2
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k] = nums1[i]; // coloca o maior elemento no fim
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }
    
    
   
};

var main = function() {
    let nums1 = [1,2,3,0,0,0];
    let m = 2;
    let nums2 = [2,5,6];
    let n = 1;
    
   merge(nums1, m, nums2, n);
    console.log(nums1);

}


main();