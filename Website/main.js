const apiUrl = "https://resthouseexam2023.azurewebsites.net/api/Houses/";

const app = Vue.createApp({
    data() 
    {
        return {
            // Get data 
            housesList: [],

            // Add data
            addedHouse: null,
            newHouse: { address: '', constructionYear: ''},

            // Delete data
            houseIdToDelete: '',
            deleteSuccess: false,
            deletedHouseId: null
               };
    },
    methods: 
    {
        async fetchHouses() 
        {
            try {
                const response = await axios.get(apiUrl);
                console.log('Response data', response.data);
                this.housesList = response.data;
            }
            catch (error)
            {
                console.error('Error fetching Houses', error);
            }
        },
        async addHouse() 
        {
            try 
            {
                const response = await axios.post(apiUrl, this.newHouse);
                this.addedHouse = response.data;
            }
            catch (error)
            {
                console.error('Error adding house', error);
            }
        },
        async deleteHouse()
        {
            try
            {
                const response = await axios.delete(apiUrl + this.houseIdToDelete);
                this.deleteSuccess = true;
                this.deletedHouseId = this.houseIdToDelete;
                // Reset form and success
                this.houseIdToDelete = '';
            }
            catch (error)
            {
                console.error('Error deleting house', error);
                this.deleteSuccess = false;
                this.deletedHouseId = null;
            }
        }
    },
    mounted()
    {
        this.fetchHouses(); // Call fetchHouses when component is mounted
    }
});

// Mount app
app.mount("#app");