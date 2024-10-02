class Constants:

    #Similarity recommendation prompts
    SIM_SYS_PROMPT = """
        You are a cinema enthusiast and the best Movie or Series recommender.
        You will take user's prompt and use it to generate up to 'Max' recommendation(s) of 'Type' that is similar to the 'Title',
        and tailored to the user's 'Likings'. Your response will be a JSON array, from [ to ] containing the title and released year.
        """

    SIM_USER1 = """
    Title: Squid Game (2021)
    Likings: Challenge, high stake and not too gore.
    Type: Movie
    Max: 5
    """

    SIM_ASSISTANT1 = """
    [
    "Alice in Borderland (2020)",
    "The Raid: Redemption (2011)",
    "The Hunger Games (2012)",
    "I Am Alive (2009)",
    "The Maze Runner (2014)"
    ]
    """

    SIM_USER2 = """
    Title: Avatar (2009)
    Likings: Great world building, beautiful environments, incredibly lifelike exotic creatures, 
    the imagery is visually, aurally and emotionally engulfing.
    Type: Movie
    Max: 10
    """

    SIM_ASSISTANT2 = """
    [
    "Dune (2021)",
    "Annihilation (2018)",
    "Pan's Labyrinth (2006)",
    "Avatar: The Way of Water (2022)",
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe (2005)",
    "Guardians of the Galaxy (2014)",
    "Valerian and the City of a Thousand Planets (2017)",
    "Prometheus (2012)",
    "Life of Pi (2012)",
    "Cloud Atlas (2012)"
    ]
    """

    SIM_USER3 = """
    Title: Your Name (2016)
    Likings: Anime, Beautiful scenery and visuals, great music, heart-touching story, happy ending.
    Type: Movie or Series
    Max: 10
    """

    SIM_ASSISTANT3 = """
    [
    "Frieren: Beyond Journey's End (2023),
    "Fruits Basket (2021)",
    "Horimiya (2021)",
    "Love, Chunibyo & Other Delusions (2012)",
    "Beyond the Boundary (2013)",
    "ReLIFE (2016)",
    "Kokoro Connect (2012)",
    "Tamako Love Story (2014)",
    "Hyouka (2012)",
    "Bakemonogatari (2009)"
    ]
    """

    #Genre recommendation prompts
    GENRE_SYS_PROMPT = """
        You are a cinema enthusiast and the best Movie or Series recommender.
        You will take user's prompt and use it to generate up to 'Max' recommendation(s) of Movie or Series that are related to the 'Keywords',
        and possess some or all of the specified 'Genre'. Your response will be a JSON array, from [ to ] containing the title and released year.
        """
    
    GENRE_USER1 = """
    Keywords: Futuristic world, alien invasion, superhumans, action packed
    Genre: Sci-fi, Action
    Type: Movie
    Max: 5
    """

    GENRE_ASSISTANT1 = """
    [
    "Edge of Tomorrow (2014)",
    "Elysium (2013)",
    "Avatar (2009)",
    "District 9 (2009)",
    "Pacific Rim (2013)"
    ]
    """

    GENRE_USER2 = """
    Keywords: Sad story, boxing
    Genre: Romance, Adventure
    Type: Series
    Max: 5
    """

    GENRE_ASSISTANT2 = """
    [
    "Million Dollar Baby (2004)",
    "The Fall (2013)",
    "Outlander (2014)",
    "Friday Night Lights (2006)",
    "This Is Us (2016)"
    ]
    """

    GENRE_USER3 = """
    Keywords: Happy loving family
    Genre: Fantasy, Comedy
    Type: Movies or Series
    Max: 5
    """

    GENRE_ASSISTANT3 = """
    [
    "Enchanted (2007)",
    "The Addams Family (2019)",
    "The Good Place (2016)",
    "Paddington (2014)",
    "The Incredibles (2004)"
    ]
    """
    
    #Random recommendation prompts
    RAND_SYS_PROMPT = """
        You are a cinema enthusiast and the best random Movie or Series recommender. 
        You will take user's prompt and use it to generate up to 'Max' random recommendation(s) of 'Category' Movie or Series. 
        Your response will be a JSON array, from [ to ] containing the title and released year.
        """
    
    RAND_USER1 = """
    Category: Popular
    Type: Movie
    Max: 5
    """

    RAND_ASSISTANT1 = """
    [
    "Inception (2010)",
    "The Dark Knight (2008)",
    "The Shawshank Redemption (1994)",
    "Pulp Fiction (1994)",
    "The Godfather (1972)"
    ]
    """

    RAND_USER2 = """
    Category: Underrated
    Type: Movie
    Max: 5
    """

    RAND_ASSISTANT2 = """
    [
    "Coherence (2013)",
    "Moon (2009)",
    "The Fall (2006)",
    "The Station Agent (2003)",
    "Frailty (2001)"
    ]
    """

    RAND_USER3 = """
    Category: Known or less known
    Type: Movie or Series
    Max: 5
    """

    RAND_ASSISTANT3 = """
    [
    "Fight Club (1999)",
    "Whiplash (2014)",
    "City of God (2002)",
    "Ikiru (1952)",
    "Spirited Away (2001)"
    ]
    """

    PAGE_LAYOUT = """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """
    GENRES = [
            'Action',
            'Adventure',
            'Animation',
            'Comedy',
            'Crime',
            'Documentary',
            'Drama',
            'Family',
            'Fantasy',
            'Film Noir',
            'Game Show',
            'Historical',
            'Horror',
            'Musical',
            'Music',
            'Mystery',
            'Romance',
            'Sci-fi',
            'Short',
            'Sport',
            'Supernatural',
            'Thriller',
            'War',
            'Western'
            ]

    DEFAULT_IMAGE = "https://www.reelviews.net/resources/img/default_poster.jpg"

    JURASSIC_PARK_POSTER = "https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_SX300.jpg"

    JURASSIC_PARK_PLOT = "A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose."

    def urlYT(key,q):
        url = f'https://www.googleapis.com/youtube/v3/search?key={key}&q={q}&type=video&parts=snippet&videoEmbeddable=true&maxResults=1'
        return url
    
    def ytEmbed(ytId):
        embed = f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{ytId}" 
                title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
                gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                """
        return embed
