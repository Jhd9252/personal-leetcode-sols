const isAnagram = (s, t) => {
    // easy check 
    if (s.length != t.length) {
        return false;
    }

    // create a HashMap
    const counter = new Map();

    for (let char of s) {
        counter.set(char, (counter.get(char) || 0) + 1);
    }

    for (let char of t) {
        // check if exists
        if (!counter.has(char) || counter.get(char) === 0) {
            return false;
        }
        counter.set(char, (counter.get(char) || 0) - 1);
    }
    return true;
}