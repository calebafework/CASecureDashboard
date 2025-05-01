<template>
    <div class="dashboard">
      <h1>CASecure Dashboard</h1>
  
      <div class="grid">
        <div class="section">
          <h2>Logs by Service</h2>
          <div v-for="(group, service) in groupedByService" :key="service">
            <h3>{{ service }}</h3>
            <ul>
              <li v-for="log in group" :key="log.id">
                [{{ log.type }}] {{ log.message }} — {{ formatTime(log.time) }}
              </li>
            </ul>
          </div>
        </div>
  
        <div class="section">
          <h2>Logs by Severity</h2>
          <div v-for="(group, type) in groupedByType" :key="type">
            <h3>{{ type }}</h3>
            <ul>
              <li v-for="log in group" :key="log.id">
                {{ log.service }}: {{ log.message }} — {{ formatTime(log.time) }}
              </li>
            </ul>
          </div>
        </div>
      </div>
  
      <div class="section chart">
        <h2>Log Volume by Type</h2>
        <BarChart :chart-data="chartData" />
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import BarChart from './BarChart.vue';
  
  export default {
    components: { BarChart },
    data() {
      return {
        logs: [],
        chartData: {
          labels: ['INFO', 'WARN', 'ERROR'],
          datasets: [{
            label: 'Log Count',
            data: [0, 0, 0],
            backgroundColor: ['#00d1b2', '#ffdd57', '#ff3860']
          }]
        }
      };
    },
    computed: {
      groupedByService() {
        return this.groupLogsBy('service');
      },
      groupedByType() {
        return this.groupLogsBy('type');
      }
    },
    methods: {
      async fetchLogs() {
        const res = await axios.get('http://localhost:5000/api/logs');
        this.logs = res.data;
        this.updateChart();
      },
      groupLogsBy(key) {
        return this.logs.reduce((groups, log) => {
          const val = log[key];
          if (!groups[val]) groups[val] = [];
          groups[val].push(log);
          return groups;
        }, {});
      },
      updateChart() {
        const count = { INFO: 0, WARN: 0, ERROR: 0 };
        this.logs.forEach(log => {
          if (count[log.type] !== undefined) count[log.type]++;
        });
        this.chartData = {
            ...this.chartData,
            datasets: [{
                ...this.chartData.datasets[0],
                data: [count.INFO, count.WARN, count.ERROR]
            }]
        };
      },
      formatTime(t) {
        return new Date(t).toLocaleTimeString();
      }
    },
    mounted() {
      this.fetchLogs();
      setInterval(this.fetchLogs, 5000);
    }
  };
</script>
<style scoped>
.dashboard {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    gap: 30px;
    align-items: center;
    /* 👈 Fix horizontal center */
}

.grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    /* 👈 Helps with centering */
    width: 100%;
}

.section {
    flex: 1 1 45%;
    background: #ffffff;
    color: #1a1a1a;
    /* 👈 Fix unreadable white-on-white */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
    min-width: 300px;
}

.chart {
    width: 100%;
    background: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}
</style>