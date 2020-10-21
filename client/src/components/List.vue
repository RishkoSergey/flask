<template>
  <v-container class="list-container">
    <v-card
      v-for="movie in movies"
      class="mb-3"
      :key="movie.id"
      color="primary"
      dark
    >
      <div class="d-flex flex-no-wrap justify-space-between">
        <div>
          <v-card-title
            class="name mb-6"
            v-text="movie.name"
          />
          <v-card-subtitle v-text="movie.country + ', ' + movie.year" />
          <v-card-subtitle class="rating" v-text="movie.rating" />
        </div>
        <v-avatar
          class="ma-3"
          width="125"
          min-width="125"
          height="180"
          tile
        >
          <v-img :src="movie.image"></v-img>
        </v-avatar>
      </div>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: 'List',
    props: ['movies']
  }
</script>

<style lang="scss">
.list-container {
  @media (min-width: 960px) {
    max-width: 800px;
  }
  @media (min-width: 1264px) {
    max-width: 900px;
  }
}
.name {
  font-weight: 400;
  line-height: 2rem;
  letter-spacing: normal !important;
  font-family: "Roboto", sans-serif !important;
  font-size: 1.5rem !important;
  @media (max-width: 1023px) {
    font-size: 1.2rem !important;
  }
  @media (max-width: 767px) {
    font-size: 1rem !important;
  }
}
.rating {
  font-size: 1.5rem !important;
  color: white !important;
}
</style>
