let logs =[];

function addLog(entry) {
    logs.unshift({
        id: logs.length + 1,
        time: new Date().toISOString(),
        ...entry,
    })
    //latest 50 logs
    logs = logs.slice(0, 50);
}

function getLogs(){
    return logs;
}

module.exports ={
    addLog,
    getLogs,
}