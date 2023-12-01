# The aspect ratio of an image describes the proportional relationship between its width and its height. Most video shown on the internet uses a 16:9 aspect ratio, which means that for every pixel in the Y, there are roughly 1.77 pixels in the X (where 1.77 ~= 16/9). As an example, 1080p video with an aspect ratio of 16:9 would have an X resolution of 1920, however 1080p video with an aspect ratio of 4:3 would have an X resolution of 1440.

# Write a function that accepts arbitrary X and Y resolutions and converts them into resolutions with a 16:9 aspect ratio that maintain equal height. Round your answers up to the nearest integer.

 function aspectRatio(x,y){
  let result = [];
  
  x = Math.ceil(y * 1.77777777);
  
  result.push(x, y);
  return result ;
}
# tested

const assert = require("chai").assert;
describe("Sample tests", () => {
  it("should work for known resolutions", () => {
    assert.deepEqual(aspectRatio(640, 480), [854,480], "x = 640, y = 480");
    assert.deepEqual(aspectRatio(960, 720), [1280,720], "x = 960, y = 720");
    assert.deepEqual(aspectRatio(1440, 1080), [1920,1080], "x = 1440, y = 1080");
    assert.deepEqual(aspectRatio(1920, 1440), [2560,1440], "x = 1920, y = 1440");
  });
});

