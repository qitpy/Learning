function maxResult(nums, k) {
    var length = nums.length;
    var maxIndex = length - 1;
    var currentIndex = 0;
    var maxResult = nums[0];

    while (currentIndex !== maxIndex) {
        var valuesAtK = [];
        var isHaveValue = false;
        for (var kIndex = 1; kIndex <= k; kIndex++) {
            var indexAtK = currentIndex + kIndex;
            if (indexAtK === maxIndex) {
                return maxResult + nums[maxIndex];
            }
            else if (nums[indexAtK] > 0) {
                maxResult += nums[indexAtK];
                currentIndex = indexAtK;
                isHaveValue = true;
                break;
            }
            else {
                valuesAtK.push(nums[indexAtK]);
            }
        }
        if (!isHaveValue) {
            const maxValue = Math.max.apply(Math, valuesAtK);
            maxResult = maxResult + maxValue;
            currentIndex = currentIndex + valuesAtK.indexOf(maxValue) + 1;
        }
    }
}

console.log(maxResult([0,-1,-2,-3,1], 2));
