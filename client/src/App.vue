<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-spacer></v-spacer>
      <v-flex xs12 sm6>
        <v-container fluid>
          <v-row>
            <v-col cols="5">
              <v-subheader class="pa-0">
                Choose country
              </v-subheader>
            </v-col>

            <v-col cols="7">
              <v-select
                v-model="selectedCountry"
                :items="countries"
                persistent-hint
                return-object
                single-line
                @change="fetchMovies"
              />
            </v-col>
          </v-row>
        </v-container>
      </v-flex>
    </v-app-bar>
    <v-main>
      <List :movies="movies" />
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';
import List from './components/List';

export default {
  name: 'App',
  components: {
    List,
  },
  data: () => ({
    selectedCountry: 'All',
    countries: [],
    movies: [],
    isEmpty: false
  }),
  methods: {
    async fetchMovies() {
      await axios.get(`http://127.0.0.1:5000//moviesByCountry?country=${this.selectedCountry}`)
        .then(res => this.movies = res.data.movies)
    }
  },
  async mounted() {
    await axios.get('http://127.0.0.1:5000/getCountries')
      .then(res => this.countries = res.data.countries);
    this.fetchMovies();
  }
};
</script>
