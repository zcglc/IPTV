// a script to arrange some irregular shapes and squares in a rectangular artboard with minimal gaps
// get the active document and the artboard
var doc = app.activeDocument;
var artboard = doc.artboards[0];

// get the shapes to arrange
var shapes = doc.selection;

// check if there are any shapes selected
if (shapes.length == 0) {
  alert("Please select some shapes to arrange.");
  exit();
}

// define a function to get the bounding box of a shape
function getBoundingBox(shape) {
  var bounds = shape.geometricBounds;
  var xMin = bounds[0];
  var yMax = bounds[1];
  var xMax = bounds[2];
  var yMin = bounds[3];
  return {xMin: xMin, yMax: yMax, xMax: xMax, yMin: yMin};
}

// define a function to get the area of a shape
function getArea(shape) {
  var bbox = getBoundingBox(shape);
  var width = bbox.xMax - bbox.xMin;
  var height = bbox.yMax - bbox.yMin;
  return width * height;
}

// define a function to sort the shapes by area in descending order
function sortByArea(shapes) {
  shapes.sort(function(a, b) {
    return getArea(b) - getArea(a);
  });
}

// define a function to split a shape into smaller rectangles
function splitShape(shape) {
  // create an array to store the rectangles
  var rectangles = [];
  
  // get the path points of the shape
  var points = shape.pathPoints;
  
  // loop through the points and create rectangles between each pair of points
  for (var i = 0; i < points.length; i++) {
    // get the current point and the next point (or the first point if it is the last point)
    var p1 = points[i];
    var p2 = points[(i + 1) % points.length];
    
    // create a rectangle with the same width and height as the distance between the two points
    var rect = doc.pathItems.rectangle(p1.anchor[1], p1.anchor[0], p2.anchor[0] - p1.anchor[0], p2.anchor[1] - p1.anchor[1]);
    
    // add the rectangle to the array
    rectangles.push(rect);
  }
  
  // return the array of rectangles
  return rectangles;
}

// define a function to check if two rectangles overlap
function overlap(rect1, rect2) {
  // get the bounding boxes of the rectangles
  var bbox1 = getBoundingBox(rect1);
  var bbox2 = getBoundingBox(rect2);
  
  // check if there is any gap between them horizontally or vertically
  if (bbox1.xMin > bbox2.xMax || bbox1.xMax < bbox2.xMin || bbox1.yMin > bbox2.yMax || bbox1.yMax < bbox2.yMin) {
    return false;
  } else {
    return true;
  }
}

// define a function to check if a rectangle fits inside the artboard
function fit(rect) {
  // get the bounding box of the rectangle and the artboard
  var bbox = getBoundingBox(rect);
  var abox = artboard.artboardRect;
  
  // check if the rectangle is within the artboard boundaries
  if (bbox.xMin >= abox[0] && bbox.xMax <= abox[2] && bbox.yMin >= abox[3] && bbox.yMax <= abox[1]) {
    return true;
  } else {
    return false;
  }
}

// define a function to arrange the rectangles in the artboard using a greedy algorithm
function arrange(rectangles) {
  
  // sort the rectangles by area in descending order
  sortByArea(rectangles);
  
  // create an array to store the placed rectangles
  var placed = [];
  
  // loop through the rectangles and try to place them in the artboard
  for (var i = 0; i < rectangles.length; i++) {
    // get the current rectangle
    var rect = rectangles[i];
    
    // try to find a position for it in the artboard that does not overlap with any placed rectangle
    var found = false;
    for (var x = artboard.artboardRect[0]; x <= artboard.artboardRect[2]; x++) {
      for (var y = artboard.artboardRect[3]; y <= artboard.art