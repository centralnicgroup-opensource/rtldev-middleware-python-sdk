## [3.5.1](https://github.com/hexonet/python-sdk/compare/v3.5.0...v3.5.1) (2020-04-30)


### Bug Fixes

* **security:** replace passwords whereever they could be used for output ([9215b87](https://github.com/hexonet/python-sdk/commit/9215b87e5353cbd2c9ce43c24099b1732104a879))

# [3.5.0](https://github.com/hexonet/python-sdk/compare/v3.4.2...v3.5.0) (2020-04-30)


### Features

* **response:** added getCommandPlain (getting used command in plain text) ([2efab17](https://github.com/hexonet/python-sdk/commit/2efab17a99402a849ad6ef712458b32a9b4594b9))

## [3.4.2](https://github.com/hexonet/python-sdk/compare/v3.4.1...v3.4.2) (2020-04-29)


### Bug Fixes

* **responsetemplatemanager:** fixed namingconventions self vs. cls ([b52b22d](https://github.com/hexonet/python-sdk/commit/b52b22d4a51c1a498870bf5b0e9a9ab73ab8ddbd))

## [3.4.1](https://github.com/hexonet/python-sdk/compare/v3.4.0...v3.4.1) (2020-04-29)


### Bug Fixes

* **messaging:** return a specific error template if API response' code or description are missing ([7cd33b4](https://github.com/hexonet/python-sdk/commit/7cd33b4cae237ae1657599a1f662ec69388971a3))

# [3.4.0](https://github.com/hexonet/python-sdk/compare/v3.3.0...v3.4.0) (2020-04-29)


### Features

* **apiclient:** support the `High Performance Proxy Setup`. see README.md ([d66d495](https://github.com/hexonet/python-sdk/commit/d66d495b0033bb9e6adcf7e9b7adb27c4eda63dd))

# [3.3.0](https://github.com/hexonet/python-sdk/compare/v3.2.2...v3.3.0) (2020-04-29)


### Features

* **apiclient:** automatic IDN conversion of API command parameters to punycode ([6562f26](https://github.com/hexonet/python-sdk/commit/6562f26c8741efa54bcf293331b8a6687b198828))

## [3.2.2](https://github.com/hexonet/python-sdk/compare/v3.2.1...v3.2.2) (2020-03-11)


### Bug Fixes

* **travis:** remove branch verification in updateVersion.sh as releasing happens on master ([4eb327e](https://github.com/hexonet/python-sdk/commit/4eb327e85e22f78d24048edaae3a175f74b3f314))

## [3.2.1](https://github.com/hexonet/python-sdk/compare/v3.2.0...v3.2.1) (2020-03-11)


### Bug Fixes

* **travis:** fixed node env usage in ci/release process ([6e8f9e0](https://github.com/hexonet/python-sdk/commit/6e8f9e0ee483e3d3d053805982e1d14647a07cc7))

# [3.2.0](https://github.com/hexonet/python-sdk/compare/v3.1.4...v3.2.0) (2020-03-11)


### Features

* **apiclient:** support bulk parameters through nested array in API command ([1e4b8e7](https://github.com/hexonet/python-sdk/commit/1e4b8e76f0f695e5e2780619b26aa0017b419b46))

## [3.1.4](https://github.com/hexonet/python-sdk/compare/v3.1.3...v3.1.4) (2019-10-04)


### Bug Fixes

* **responsetemplate/mgr:** improve description for `423 Empty API response` [HM-577] ([7bbcee9](https://github.com/hexonet/python-sdk/commit/7bbcee9))
* **responsetemplate/mgr:** pep8 review of response description usage ([1410e58](https://github.com/hexonet/python-sdk/commit/1410e58))

## [3.1.3](https://github.com/hexonet/python-sdk/compare/v3.1.2...v3.1.3) (2019-09-24)


### Bug Fixes

* **Travis:** fixed pip calls ([479cd06](https://github.com/hexonet/python-sdk/commit/479cd06))
* **Travis:** upgrade packages in build ([3756193](https://github.com/hexonet/python-sdk/commit/3756193))

## [3.1.2](https://github.com/hexonet/python-sdk/compare/v3.1.1...v3.1.2) (2019-09-19)


### Bug Fixes

* **release process:** migrate configuration ([9fcd7d1](https://github.com/hexonet/python-sdk/commit/9fcd7d1))

## [3.1.1](https://github.com/hexonet/python-sdk/compare/v3.1.0...v3.1.1) (2019-08-16)


### Bug Fixes

* **APIClient:** update default SDK url ([758bf13](https://github.com/hexonet/python-sdk/commit/758bf13))

# [3.1.0](https://github.com/hexonet/python-sdk/compare/v3.0.2...v3.1.0) (2019-04-16)


### Features

* **responsetemplate:** add isPending method ([c429972](https://github.com/hexonet/python-sdk/commit/c429972))

## [3.0.2](https://github.com/hexonet/python-sdk/compare/v3.0.1...v3.0.2) (2019-04-04)


### Bug Fixes

* **APIClient:** return APIClient instance in setUserAgent method ([2169891](https://github.com/hexonet/python-sdk/commit/2169891))

## [3.0.1](https://github.com/hexonet/python-sdk/compare/v3.0.0...v3.0.1) (2019-04-01)


### Bug Fixes

* **docs:** remove python 2 documentation from docs ([81a4586](https://github.com/hexonet/python-sdk/commit/81a4586))

# [3.0.0](https://github.com/hexonet/python-sdk/compare/v2.1.2...v3.0.0) (2019-04-01)


### Code Refactoring

* **pkg:** python 2 support removal ([11351aa](https://github.com/hexonet/python-sdk/commit/11351aa))


### BREAKING CHANGES

* **pkg:** drop python 2 support

## [2.1.2](https://github.com/hexonet/python-sdk/compare/v2.1.1...v2.1.2) (2019-04-01)


### Bug Fixes

* **apiclient:** fix usage of user agent header field ([bbd9095](https://github.com/hexonet/python-sdk/commit/bbd9095))

## [2.1.1](https://github.com/hexonet/python-sdk/compare/v2.1.0...v2.1.1) (2019-03-29)


### Bug Fixes

* **apiclient:** fix useragent string. missing semicolon ([8161b41](https://github.com/hexonet/python-sdk/commit/8161b41))

# [2.1.0](https://github.com/hexonet/python-sdk/compare/v2.0.2...v2.1.0) (2019-03-29)


### Features

* **apiclient:** review useragent support ([4b4d9a7](https://github.com/hexonet/python-sdk/commit/4b4d9a7))

## [2.0.2](https://github.com/hexonet/python-sdk/compare/v2.0.1...v2.0.2) (2019-03-06)


### Bug Fixes

* **response:** remove deprecated debug outputs ([70dbe7e](https://github.com/hexonet/python-sdk/commit/70dbe7e))

## [2.0.1](https://github.com/hexonet/python-sdk.git/compare/v2.0.0...v2.0.1) (2018-10-31)


### Bug Fixes

* **releasing:** moved travis deploy step into semantic release ([c1a3415](https://github.com/hexonet/python-sdk.git/commit/c1a3415))

# [2.0.0](https://github.com/hexonet/python-sdk.git/compare/v1.2.7...v2.0.0) (2018-10-31)


### Bug Fixes

* **semantic-release:** missing setup ([f100c3e](https://github.com/hexonet/python-sdk.git/commit/f100c3e))


### Code Refactoring

* **pkg:** migrate to cross-SDK UML diagram ([52a78a2](https://github.com/hexonet/python-sdk.git/commit/52a78a2))


### BREAKING CHANGES

* **pkg:** rewrite from scratch to align the structure of our SDKs; downward incompatible
