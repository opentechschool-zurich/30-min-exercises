function get_inverted_time(now) {
  const hours = now.getHours()
  const minutes = now.getMinutes()
  const seconds = now.getSeconds()

  let inverted_seconds = 0
  if (seconds > 0) {
    inverted_seconds = 60 - seconds
  }
  
  let inverted_minutes = 0
  if (minutes > 0 || seconds > 0) {
    inverted_minutes = 60 - minutes
    if (seconds > 0) {
      inverted_minutes = inverted_minutes - 1
    }
  }
  let inverted_hours = 24 - hours
  if (minutes > 0 || seconds > 0) {
    inverted_hours = inverted_hours - 1
  }
  return [inverted_hours, inverted_minutes, inverted_seconds]
}


const interval = setInterval(function() {
  console.clear()
  const now = new Date()
  const [hours, minutes, seconds] = get_inverted_time(now)
  console.log(hours, minutes, seconds)
}, 1000);

// clearInterval(interval);
  
{
  const now = new Date()
  now.setHours(20, 19, 25)
  const [hours, minutes, seconds] = get_inverted_time(now)
  // console.log(hours, minutes, seconds)
  console.assert(hours == 3)
  console.assert(minutes == 40)
  console.assert(seconds == 35)
}

{
  const now = new Date()
  now.setHours(20, 0, 0)
  const [hours, minutes, seconds] = get_inverted_time(now)
  // console.log(hours, minutes, seconds)
  console.assert(hours == 4)
  console.assert(minutes == 0)
  console.assert(seconds == 0)
}

{
  const now = new Date()
  now.setHours(20, 0, 10)
  const [hours, minutes, seconds] = get_inverted_time(now)
  // console.log(hours, minutes, seconds)
  console.assert(hours == 3)
  console.assert(minutes == 59)
  console.assert(seconds == 50)
}

// 20 19 25
// console.log(hours, minutes, seconds)
// 03 40 35
// console.log(inverted_hours, inverted_minutes, inverted_seconds)
// console.clear()
