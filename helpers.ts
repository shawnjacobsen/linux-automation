require('dotenv').config()

// assume production build if env variable is missing
export const isProduction = () => !process.env.PRODUCTION || Number.parseInt(process.env.PRODUCTION) === 1
export const isNumber = (test:string):boolean => {return /^\d+$/.test(test)}

export const productionLog = (message:string=""):void => {
  if (isProduction()) {
    // TODO
    // production log to some log system
  } else {
    console.log("\n-------------")
    console.log(message)
    console.log("-------------")
  }
}


export const filterKeysOfObject = (obj:Object, allowed:Array<any>) => {
  return Object.keys(obj).filter(key => 
    allowed.includes(key)).reduce((prevObj, key) => {
    prevObj[key] = obj[key]
    return prevObj
    },
    {})
}