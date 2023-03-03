// Recursive
const quickSort = (arr) => {
	// Input: Array
	// If the array size is less than 1, return
	if (arr.length < 2) {
		return arr;
	}
	// Pick a pivot
	const pivot = arr[0];
	// Create an array for values smaller than the pivot
	let smallerArr = [];
	// Create an array for values larger than the pivot
	let largerArr = [];
	// Sort values in comparison to pivot
	for (let i = 1; i < arr.length; i++) {
		if (arr[i] < pivot) {
			smallerArr.push(arr[i]);
		} else {
			largerArr.push(arr[i]);
		}
	}
	// Return recursive quickSort on the smallerArr + pivot + recursive quicksort on largerArr
	return [...quickSort(smallerArr), pivot, ...quickSort(largerArr)];
	// Output: sorted array
};

let arr = [13, 46, 8, 9, 4, 2, 77, 62, 99, 1, 47];
console.log(quickSort(arr));
