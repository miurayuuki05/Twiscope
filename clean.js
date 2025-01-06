const fs = require("fs");

data = fs.readFileSync("tweets.json");

data = JSON.parse(data);

function removeDuplicates(data) {
  let unique = {};
  data.forEach((tweet) => {
    unique[tweet] = 0;
  });

  return Object.keys(unique);
}

data = removeDuplicates(data);

fs.writeFileSync("tweetsclean.json", JSON.stringify(data), "utf-8");