 <table>
    <tr>
      <td> <img src="icon.png" width="128" alt="fastlane Logo" /> </td>
      <td valign="center"> <h1> alfred-fastlane </h1> </td>
    </tr>
</table>


## Search and execute Fastlane lanes directly from Alfred

### Features
* ✅ Fuzzy matching
* ✅ Automatically detects frontmost Xcode project
* ✅ Default project path
* ✅ Optional caching for remote lanes
* ✅ Supports arguments
* ✅ In-Alfred settings flow

### Usage
* `Toggle Alfred` → type `fl` → select a path containing a Fastlane folder → `↩︎`
* While selecting a lane, hold `⌘` to toggle between `bundle exec fastlane [lane]` and `fastlane [lane]`
* Hold `⌥` or `⇧` to execute selected lane with arguments
* Lanes contained within the `default path` will be shown right after typing `fl`, without having to select the folder first
* `default path` can either be set via `fl set` or by `'[selected lane]' lanes:` `↩︎`
* With a Xcode project open, the corresponding project path will be used as `default path` (alternatively, press `⌘`+`⇧`+`⌃`+`o` while focusing Xcode)

## Acknowledgements:

* [alfred-fuzzy](https://github.com/deanishe/alfred-fuzzy) by Dean Jackson 
* [alfred-workflow](https://github.com/deanishe/alfred-workflow) by Dean Jackson

##

*Fastlane © Google, Inc. All Rights Reserved*

**This project is in no way affiliated with Google Inc.**
