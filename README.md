 <table>
    <tr>
      <td> <img src="icon.png" width="128" alt="fastlane Logo" /> </td>
      <td valign="center"> <h1> alfred-fastlane </h1> </td>
    </tr>
</table>

## Search, select and execute [Fastlane](https://fastlane.tools/) lanes directly from [Alfred](https://www.alfredapp.com/)


https://user-images.githubusercontent.com/2648540/155036474-2534e50a-7afb-474a-8d41-0b13bdab1207.mp4


### Features
* ✅ Scrapes lanes from Fastfile
* ✅ Optional caching for remote lanes
* ✅ Auto-detects open Xcode project
* ✅ Fuzzy matching
* ✅ Supports parameters
* ✅ In-Alfred settings flow

### Getting started
* `Toggle Alfred` → type `fl` → select path containing Fastlane folder `↩︎`
* With lane selected, hold `⌘` to toggle between `bundle exec fastlane [lane]` and `fastlane [lane]`
* Hold `⌥` or `⇧` to pass parameters to selected lane
* Lanes contained within the `default path` will be shown right after typing `fl`
* `default path` can either be set via `fl set` or by `'[selected path]' lanes:` `↩︎`
* The frontmost open Xcode project is automatically used as `default path` (alternatively, press `⌃⇧⌘O` in Xcode)


[Thread on alfredforum.com](https://www.alfredforum.com/topic/18016-fastlane-search-select-and-execute-fastlane-lanes/)

## Acknowledgements:

* [Fastlane](https://github.com/fastlane/fastlane) by [Fastlane team](https://github.com/fastlane/fastlane#fastlane-team) & especially [Felix Krause](https://twitter.com/KrauseFx)
* [alfred-fuzzy](https://github.com/deanishe/alfred-fuzzy) by Dean Jackson 
* [alfred-workflow](https://github.com/deanishe/alfred-workflow) by Dean Jackson

##

*Fastlane © Google, Inc. All Rights Reserved*

**This project is in no way affiliated with Google Inc.**
