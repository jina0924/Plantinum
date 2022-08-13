<template>
  <div>
    <nav-bar></nav-bar>
    <leaf-82-search-bar :limit="limit" ></leaf-82-search-bar>
    <leaf-82-list :sellItems="sellItems" :buyItems="buyItems"></leaf-82-list>
    <!-- <leaf-82-list></leaf-82-list> -->
    <div class="d-flex justify-content-center">
      더보기
    </div>
  </div>
</template>

<script>
import Leaf82SearchBar from '@/components/Leaf82SearchBar.vue'
import Leaf82List from '@/components/Leaf82List.vue'
import NavBar from '@/components/NavBar.vue'
import { mapActions , mapGetters } from 'vuex'

export default {
  name: 'Leaf82View',
  components: {
    NavBar,
    Leaf82SearchBar,
    Leaf82List,
  },
  data(){
    return {
      sellItems: [],
      buyItems: [],
      limit: 2,
      loadPage: 1,
      searchPage: 1
    }
  },
  methods: {
    ...mapActions(['fetchLeaf82', 'fetchSido']),
    sortList(items) {
      this.sellItems = []
      this.buyItems = []
      for (let item of items.results) {
        if (item.category_class === '분양해요') {
          this.sellItems.push(item)
        } else {
          this.buyItems.push(item)
        }
      }
    },
    trimItems(sellItems, buyItems) {
      for (let item of sellItems) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
      for (let item of buyItems) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
    },
    beforeFetchLeaf82() {
      const params = {
        page: 1,
        limit: 2,
      }
      this.fetchLeaf82(params)
    }
  },
  computed: {
    ...mapGetters(['searchList'])
  },
  created() {
    this.beforeFetchLeaf82()
    this.fetchSido()
  },
  watch: {
    searchList: function() {
      this.sortList(this.searchList)
      this.trimItems(this.sellItems, this.buyItems)
    }
  }
}
</script>

<style scoped>
div {
  background-color: #F8F5EE;
}
</style>