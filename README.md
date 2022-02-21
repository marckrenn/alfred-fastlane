 <table>
    <tr>
      <td> <img src="icon.png" width="128" alt="fastlane Logo" /> </td>
      <td valign="center"> <h1> alfred-fastlane </h1> </td>
    </tr>
</table>

## Search, select and execute Fastlane lanes directly from Alfred


https://user-images.githubusercontent.com/2648540/155036474-2534e50a-7afb-474a-8d41-0b13bdab1207.mp4


### Features
* ✅ Dynamically scrapes Fastfile
* ✅ Optional caching for remote lanes
* ✅ Automatically detects open Xcode project
* ✅ Default project path
* ✅ Fuzzy matching
* ✅ Supports parameters
* ✅ In-Alfred settings flow

### Usage
* `Toggle Alfred` → type `fl` → select path containing Fastlane folder `↩︎`
* With lane selected, hold `⌘` to toggle between `bundle exec fastlane [lane]` and `fastlane [lane]`
* Hold `⌥` or `⇧` to pass parameters to selected lane
* Lanes contained within the `default path` will be shown right after typing `fl`
* `default path` can either be set via `fl set` or by `'[selected path]' lanes:` `↩︎`
* The frontmost open Xcode project is automatically used as `default path` (alternatively, press `⌃⇧⌘O` in Xcode)

## Acknowledgements:

* [Fastlane](https://github.com/fastlane/fastlane) by [Fastlane team](https://github.com/fastlane/fastlane#fastlane-team) & especially [Felix Krause](https://twitter.com/KrauseFx)
* [alfred-fuzzy](https://github.com/deanishe/alfred-fuzzy) by Dean Jackson 
* [alfred-workflow](https://github.com/deanishe/alfred-workflow) by Dean Jackson

##

*Fastlane © Google, Inc. All Rights Reserved*

**This project is in no way affiliated with Google Inc.**
