function maxResult(nums: number[], k: number): number {
    const length = nums.length;
    const maxIndex = length - 1;
    let currentIndex = 0;
    let maxResult = nums[0];
    
    while (currentIndex !== maxIndex) {
        
        console.log("currentIndex", currentIndex);
        const valuesAtK: number[] = []
        for (let kIndex = 1; kIndex <= k; kIndex++) {
            const indexAtK: number = currentIndex + kIndex;
            console.log("indexAtK", indexAtK);
            if (indexAtK === maxIndex) {
                console.log("indexAtK == maxIndex", maxResult + nums[maxIndex])
                return maxResult + nums[maxIndex]
            } 
            if (nums[indexAtK] > 0) {
                console.log("value at K > 0, maxResult", maxResult)
                maxResult += nums[indexAtK];
                currentIndex = indexAtK;
                break;
            }
            else {
                valuesAtK.push(nums[indexAtK]);
                console.log("push to valuesAtK", nums[indexAtK])
            }
        }
        const maxValue = Math.max(...valuesAtK);
        console.log("Arr: ", valuesAtK, "maxValue", maxValue)
        currentIndex = currentIndex + valuesAtK.indexOf(maxValue);
        maxResult += maxValue;
        console.log("maxResult & currentIndex", maxResult, currentIndex)
    }
    return maxResult;
};

console.log(maxResult([1,-1,-2,4,-7,3], 2));