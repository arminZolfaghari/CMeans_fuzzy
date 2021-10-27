



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">CMeans_fuzzy</h2>
  <p align="center">
    Classification based on Fuzzy Logic(C-Means).
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Fuzzy-CMeans-Algorithm"></a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#Sample-Of-Output">Getting Started</a>
      <ul>
        <li><a href="#Normal-Clustering-(dataset1)">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Computational Intelligence Course 2nd Project:
In this project the `Fuzzy` version of `K-Means` algorithm is implemented. Each datapoint isn't forced to belong only to a specific cluster, but can belong to clusters to `Verying Degrees`. Thats difference between `Fuzzy Clustering` and `Normal Clustering`.

### Fuzzy CMeans Algorithm:
1. Determine the number of clusters, then Generate the centroid of clusters randomly.
2. Finding each data point belongs to which cluster (or clusters).
3. Updating new centroid of clusters based on datapoints in the cluster.
4. Repeat steps 2 and 3 until each cluster reaches stability.


### Built With
* [python](https://python.org/)





<!-- GETTING STARTED -->
## Getting Started
### Installation
1. Clone the repository
```sh
   git clone https://github.com/arminZolfaghari/CMeans_fuzzy.git
   ```
2. Run CMeans.py with ```python CMeans.py```



## Sample Of Output
### Normal Clustering (dataset1)
![alt text](https://github.com/arminZolfaghari/CMeans_fuzzy/blob/main/sample_run/sampleRun-normalClustring-dataset1.png)

### Fuzzy Clustering (dataset1)
![alt text](https://github.com/arminZolfaghari/CMeans_fuzzy/blob/main/sample_run/sampleRun-fuzzyClustring-dataset1.png)



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Armin Zolfaghari Daryani - arminzolfagharid@gmail.com
Project Link: [https://github.com/arminZolfaghari/CMeans_fuzzy](https://github.com/arminZolfaghari/CMeans_fuzzy)
<p align="right">(<a href="#top">back to top</a>)</p>

