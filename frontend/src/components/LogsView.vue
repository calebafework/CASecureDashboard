<template>
  <div class="logs-container">
    <h1>System Logs</h1>
    <button @click="fetchLogs">Refresh Logs</button>
    <ul>
      <li v-for="log in logs" :key="log.id">
        <strong>[{{ log.type }}]</strong> {{ log.message }} — <small>{{ formatTime(log.time) }}</small>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LogsView',
  data() {
    return {
      logs: []
    };
  },
  methods: {
    async fetchLogs() {
      try {
        const res = await axios.get('http://localhost:5000/api/logs');
        this.logs = res.data;
      } catch (error) {
        console.error('Failed to fetch logs:', error);
      }
    },
    formatTime(timeString) {
      return new Date(timeString).toLocaleString();
    }
  },
  mounted() {
    this.fetchLogs();
    setInterval(this.fetchLogs, 5000); // Auto-refresh logs every 5 seconds
  }
};
</script>

<style scoped>
.logs-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin-bottom: 10px;
  background: #000000;
  padding: 10px;
  border-radius: 5px;
}
</style>
