int equilibriumPoint(std::vector<int> arr) {
    // If there is only a single element in the array, then the answer is 1.
    if (arr.size() == 1)
        return 1;

    // We need to keep track of the running total and the overall total.
    int runningTotal = 0;
    int overallTotal = std::accumulate(arr.begin(), arr.end(), 0);

    // Loop through the entire array. There is probably a more efficient break
    // out of the loop earlier, but it would be O(n) regardless.
    for (int i = 0; i < arr.size(); ++i) {
        // Get the current element to subtract from the overal total.
        int currentElement = arr[i];

        // If the running total is half of the difference of the overal total
        // and the current element, then `i` is our equilibrium point.
        if (overallTotal - currentElement == runningTotal * 2)
            return (i + 1);

        // Since the equilibrium point was not found, add the current element
        // to the running total and move onto the next element.
        runningTotal += currentElement;
    }

    // No equilibrium point was found.
    return -1;
}

